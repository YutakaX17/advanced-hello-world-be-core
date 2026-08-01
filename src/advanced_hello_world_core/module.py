import re
from dataclasses import dataclass

MODULE_CONTRACT_VERSION = 1

_MODULE_ID = re.compile(r"^[a-z][a-z0-9-]*$")
_IMPORT_PATH = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*(\.[A-Za-z_][A-Za-z0-9_]*)*$")


@dataclass(frozen=True, slots=True)
class BackendModule:
    """Stable metadata exported by an installable backend feature package."""

    id: str
    django_app: str
    urls: str | None = None
    url_prefix: str = "api/"
    contract_version: int = MODULE_CONTRACT_VERSION

    def __post_init__(self) -> None:
        if not _MODULE_ID.fullmatch(self.id):
            raise ValueError("module id must use lower-case letters, digits, and hyphens")
        if not _IMPORT_PATH.fullmatch(self.django_app):
            raise ValueError("django_app must be a dotted Python import path")
        if self.urls is not None and not _IMPORT_PATH.fullmatch(self.urls):
            raise ValueError("urls must be a dotted Python import path")
        if self.url_prefix.startswith("/") or not self.url_prefix.endswith("/"):
            raise ValueError("url_prefix must be relative and end with '/'")
        if self.contract_version != MODULE_CONTRACT_VERSION:
            raise ValueError(f"unsupported backend module contract: {self.contract_version}")
