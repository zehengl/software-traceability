datasets
========

## repo

* cm1
* cm1_sub
* gantt
* modis
* pine
* wvcchit

## structure

```
.
├── /high/...
├── /low/...
└── /trace.json
```

### high/

* This folder contains all high-level software artifacts.

### low/

* This folder contains all low-level software artifacts.

### trace.json

* This file contains the traceability matrix between high- and low- level software artifacts.
* Each key represents a high-level artifact and pairs with an array of low-level artifacts that the high-level one can be traced to. 
* If an array is empty, that high-level artifact cannot be traced to any low-level artifacts.