# Configuration

The client reads configuration from three different locations.

* `defaults.cfg` bundled in client.
* `.bdss.cfg` in the current user's home directory.
* `bdss.cfg` in the current working directory.

Each file overrides the last. So if an option is set to one value in `defaults.cfg` and another value
in `~/.bdss.cfg`, the client will use the value set in `~/.bdss.cfg`.

The file should look like:

```ini
[metadata_repository]
url=http://localhost:5000
```

## Available Options

* `metadata_repository`

    * `url` The URL of the metadata repository to use.