# Touch Logger
A touch component that can be used to log to the textport and to file. This Logger is designed to be used in applications that run for a prolonged period of time and need to have good historical records.

## Installing
This repository uses git submodules. After cloning, please run `git submodule update --init --recursive`.

## Usage
To use the logger, grab the release `release/Logger.tox`. This can then be included in any touch project. 

### Configuration
To use the logger, configure the settings in the components `Logger` page.
* `Logging Level` is the minimum level that will actual be logged out. Anything lower than the selected will neither be written to the textport or the log file.
* `Rotate File` is used to write each day to its own file. When enabled, a file will be created with the following format `{specified log folder}/{two digit month}/{full year}-{two digit month}-{two digit day}`
* `Time Format` specifies whether the timestamps used will be using UTC or the local time as configured by the PC.

### API
The logger is designed to work very similarly to [logging in cinder](https://libcinder.org/docs/guides/logging/index.html). 

```python
# log out using the level you wish
op.log.Verbose("message")
op.log.Debug("message")
op.log.Info("message")
op.log.Warning("message")
op.log.Error("message")
op.log.Fatal("message")
# compose message with dynamic level. The second argument is the lowercase string representation of the level
op.log.ComposeLog("message", "info")
# set the logging level
op.log.SetLevel("info")
```
