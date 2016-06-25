## Using these examples in place

To verify that the example works within the phenopacket-python directory:

```
cd phenopacket-python/
source env/bin/activate # Or whatever equivalent is used to establish a Python environment
cd examples/
python gen_journal_packet.py

```

The output from `gen_journal_packet.py` should resemble:

```
{
  "entities": [
    {
      "id": "http://monarchinitiative.org/patient/1",
      "type": "patient"
    },
    {
      "id": "http://monarchinitiative.org/patient/2",
      "type": "patient"
    }
  ],
  "id": "packet1",
  "phenotype_profile": [
    {
      "entity": "http://monarchinitiative.org/patient/1",
      "phenotype": {
        "environment": {},
        "offset": {},
        "onset": {},
        "severity": {}
      }
    }
  ],
  "title": "Fatal infantile mitochondrial encephalomyopathy, hypertrophic cardiomyopathy and optic atrophy associated with a homozygous OPA1 mutation"
```


## Using these examples from a different project or directory

Until the `phenopacket-python` package is distributed via [PyPi](https://pypi.python.org/pypi), the easiest way to use the package is to install the repo locally and to adjust your `PYTHONPATH` environment variable to include the repo's directory. For example, suppose that the `phenopacket-python` repo is located in `~/phenopacket-python` and that you have a directory `~/phenopacket-example` where you want to build a test program. For this example, we will copy the `gen_journal_packet.py` example as our test program.


```
cd ~/phenopacket-python
source env/bin/activate # Or whatever equivalent is used to establish a Python environment
python setup.py install
cd ~/phenopacket-example
cp ~/phenopacket-python/examples/gen_journal_packet.py ./
PYTHONPATH=$PYTHONPATH:~/phenopacket-python python gen_journal_packet.py
```

