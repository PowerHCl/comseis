# comseis innovation project

## data download
### Wave data
- use [Standing Order for Data(SOD)](https://www.seis.sc.edu/sod/) to download all repeat-earthquake waveform in global stations.
### Instrument response file
- use FetchData command line tool (designed by IRIS DMC（Data Management Center)) to download instrument response file
### Mark P-wave arrival time
- use [Taup](https://www.seis.sc.edu/taup/) software

### cross-correlate
R_{fg}[n] = \sum_{m=-\infty}^{\infty} f[m] \cdot g[m + n]
