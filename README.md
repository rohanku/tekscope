# `tekscope`
API for interacting with Tektronix oscilloscopes.

## Installation

Install the package by cloning the repository and installing with `pip` from the package root.

```
git clone https://github.com/rohanku/tekscope.git
cd tekscope && pip install -e .
```

## Basic usage

This library assumes that the oscilloscope is connected to the desired device via Ethernet and has its socket server enabled. By default, the oscillocsope is assumed to be listening at address `169.254.8.194:4000`, but this setting can be overriden if needed.

### CLI

Installing the package also installs a binary to path that enables interacting with an oscilloscope via the command line. For example, the following command will transfer all waveforms in the current acquisition from the oscilloscope to a local file called `data.tek`:

```bash
tekscope transfer -a -o data.tek
```

The resulting waveforms can be viewed with the following command:

```bash
tekscope display data.tek
```

### Python library

The CLI has an underlying Python library that can be used to interface with the oscillocsope programmatically. It can also be used to process data retrieved from the oscilloscope via the CLI.

If you would like to understand the API in more depth, please look at the type signatures and comments in [`waveform.py`](tekscope/waveform.py) and [`__init__.py`](tekscope/__init__.py) (specifically the `Waveform*` types and the `retrieve_waveform` and `retrieve_all_waveforms` functions). It might also help to look at [`io.py`](tekscope.io.py) to see how the saving and loading APIs are defined.

#### Examples

```python
"""
Data retrieval and processing example.
"""
import tekscope
from tekscope import Oscilloscope

osc = Oscilloscope(host="169.254.8.194", port=4000)

wfs = osc.retrieve_all_waveforms()

# Plot the CH1 analog waveform
wf1 = wfs.get("CH1")
plt.plot(wf1.time(), wf1.voltage(), label=wf1.channel)

# Plot the D0 digital waveform
wf2 = wfs.get("D0")
plt.plot(wf2.time(), wf2.voltage(), label=wf2.channel)

# Save all waveforms to `data.tek`
tekscope.io.save_waveforms(wfs, "data.tek")
```

```python
"""
Data loading example.
"""

import tekscope

wfs = tekscope.io.load_waveforms("data.tek")

# Plot the CH1 analog waveform
wf1 = wfs.get("CH1")
plt.plot(wf1.time(), wf1.voltage(), label=wf1.channel)

# Plot the D0 digital waveform
wf2 = wfs.get("D0")
plt.plot(wf2.time(), wf2.voltage(), label=wf2.channel)
```
