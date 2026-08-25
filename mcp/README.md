# Vault MCP Foundation

`scripts/vault-mcp.py` is a local, read-only stdio MCP adapter for compact Vault discovery and selection.

Current tool families include:

- Vault search
- interactive effect lookup / selection / skill generation
- immersive template lookup / selection / skill generation
- **3D mode lookup and classification**
- 3D production-resource lookup / selection / skill generation
- 3D delivery-runtime lookup / selection / skill generation

Important 3D tools:

```text
get_3d_mode
classify_3d_mode
get_3d_production_resource
select_3d_production_resource
get_3d_production_skill
get_3d_delivery_runtime
select_3d_delivery_runtime
get_3d_delivery_skill
```

`select_3d_delivery_runtime` requires an already-classified `mode`. This prevents an MCP-capable agent from treating an available GLB/GLTF as permission to add free rotation or configuration.

Example logic:

```text
classify_3d_mode("users swipe/drag mannequin 360 to inspect dress")
→ inspectable-object

select_3d_delivery_runtime(
  need="rotate and inspect verified dress mannequin",
  mode="inspectable-object",
  format="glb"
)
→ bounded model-viewer profile when sufficient
```

The adapter deliberately does not perform business-source web research, write files, install Blender resources, host a remote service, approve third-party asset rights or bypass authentication/entitlements.

Run:

```bash
python scripts/vault-mcp.py
```

from a client configured for local stdio MCP servers.
