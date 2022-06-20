# fake classification data

This is a small and silly project to generate some realistic but fake binary classification predictions and labels for use in [metrics](https://github.com/cjwallace/metrics). It's unlikely you will have any use for this, but if you do, clone the repo, then run

```bash
cd fake-classification-data
poetry install
poetry run generate
```

A `predictions.json` file will be created in `/data` with some prediction probabilities and labels. It'll be structured appropriately for consumption by the metrics JSON upload:

```JSON
[
  {
    "probability": 0.10,
    "label": 0
  },
  {
    "probability": 0.46,
    "label": 1
  },
  ...
]
```

✌️