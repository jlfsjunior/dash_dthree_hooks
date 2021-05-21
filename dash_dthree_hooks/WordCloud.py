# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class WordCloud(Component):
    """A WordCloud component.
WordCloud component using d3 and hooks

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- clicked (dict; optional):
    Clicked word object (from d3).

- clickedTimestamp (number; optional):
    Clicked timestamp.

- data (list; optional):
    Data.

- selected (list of numbers; optional):
    Array containing selected items Defaults to empty array.

- style (dict; default {    padding: 5,    fillRegular: 'black',    fillHover: 'gray',    fillSelected: 'red',    fontFamily: 'Cera Pro, Noto Sans',    fontSizeMin: 16,    fontSizeMax: 40,    fontSizeScale: 'linear', // log or sqrt    transitionDuration: 500,}):
    Chart style.

- wrapperStyle (dict; optional):
    wrapper div style."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, data=Component.UNDEFINED, clicked=Component.UNDEFINED, clickedTimestamp=Component.UNDEFINED, selected=Component.UNDEFINED, style=Component.UNDEFINED, wrapperStyle=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'clicked', 'clickedTimestamp', 'data', 'selected', 'style', 'wrapperStyle']
        self._type = 'WordCloud'
        self._namespace = 'dash_dthree_hooks'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'clicked', 'clickedTimestamp', 'data', 'selected', 'style', 'wrapperStyle']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(WordCloud, self).__init__(**args)
