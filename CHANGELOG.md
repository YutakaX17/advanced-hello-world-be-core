# Changelog

## 0.3.0

- Move message persistence and REST behavior to the independently versioned
  messages module.
- Preserve the historical message table and all existing rows through a
  state-only migration.
- Publish inline type information for downstream module packages.

## 0.2.0

- Add the stable version-one backend module metadata contract.
- Validate module identifiers, Django application paths, URL paths, prefixes,
  and contract versions.

## 0.1.0

- Publish the initial reusable message API and health endpoints.
