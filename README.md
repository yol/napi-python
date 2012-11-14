maluuba_napi
===========

Maluuba nAPI is a new API that allows developers to add Natural Language Understanding (NLU)
to their software.

Features
--------

This API currently supports 22 different domains and around 70 different intents or actions.
We also parse out numerous entities. We believe that this API is the beginning of something great,
something that is going to completely change how people interact with their devices. But it is
just a beginning. We are starting out with the given domains, but plan on massively expanding it as
feature requests come in, and we see how people want to use this technology.

Access
------

Please sign up at the [Maluuba Developer Site](http://developer.maluuba.com) and apply for access.
We are currently in an alpha stage right now, and giving out API keys to interested third parties.
Once you have been approved, you will receive an API key that you can use with this client.

Installation
------------

To install the nAPI client for Python, you can simply:

```
pip install maluuba_napi
```

Usage
-----

Here's a simple example using the Maluuba nAPI to categorize and extract information about a
naturally-spoken sentence:

```python
>>> from maluuba_napi import client
>>> c = client.NAPIClient('YOUR-API-KEY-HERE')
>>> r = c.interpret('Set up a meeting with Bob tomorrow night at 7 PM to discuss the TPS reports')
>>> r.category
u'CALENDAR'
>>> r.action
u'CALENDAR_CREATE_EVENT'
>>> pp.pprint(r.entities)
{   u'contacts': [{   u'name': u'bob'}],
    u'dateRange': [   {   u'end': datetime.date(2012, 11, 16),
                          u'start': datetime.date(2012, 11, 15)}],
    u'timeRange': [   {   u'end': datetime.time(19, 0),
                          u'start': datetime.time(19, 0)}],
    u'title': [u'meeting to discuss the tps reports']}
```