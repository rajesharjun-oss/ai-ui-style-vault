# Vault MCP Foundation

`scripts/vault-mcp.py` is a local, read-only stdio MCP adapter. It exposes:

- `search_vault`
- `get_effect_contract`
- `select_interactive_effect`
- `get_effect_skill`

It deliberately does not perform business-source web research, write files, host a remote service or bypass third-party authentication/entitlements.

Run:

```bash
python scripts/vault-mcp.py
```

from a client configured for local stdio MCP servers.
