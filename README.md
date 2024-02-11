# ofac-sdn-analysis
This project is to download, parse and analyse the OFAC SDN list.

### Usage
----------------------
To load the [OFAC'S SANCTIONS LISTS](https://sanctionssearch.ofac.treas.gov/) and parse to dictionay format.

#### Indivisual List  

```python
>>> from sdnloader import load
>>> loader = load.sdn()
>>> ind_list = loader.individual_list()
>>> print(ind_list)
[{'profile_id': '2674', 'first_name': 'ABBAS', 'last_name': 'Abu'}, ... ]
```

#### Organization List  

```python
>>> from sdnloader import load
>>> loader = load.sdn()
>>> org_list = loader.organization_list()
>>> print(org_list)
[{'profile_id': '36', 'organization_name': 'AEROCARIBBEAN AIRLINES'}, ... ]
```

## Test

```shell:
$ python -m unittest tests.test_load
```

## Reference
* [SEARCH OFAC'S SANCTIONS LISTS](https://sanctionssearch.ofac.treas.gov/)
* [Specially Designated Nationals List - Data Formats & Data Schemas](https://ofac.treasury.gov/specially-designated-nationals-list-data-formats-data-schemas)
* [Explanatory Documentation for Advanced Sanctions Data Model format​](https://ofac.treasury.gov/media/10391/download?inline)
* [OpenSanctions](https://www.opensanctions.org/)