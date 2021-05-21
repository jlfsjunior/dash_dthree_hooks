# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Bubble(Component):
    """A Bubble component.
Bubble component using d3 and hooks

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- clicked (dict; optional):
    Clicked datum (use in point click callbacks).

- data (list; optional):
    Data.

- height (number; optional):
    Chart height.

- width (number; optional):
    Chart width."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, data=Component.UNDEFINED, clicked=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'clicked', 'data', 'height', 'width']
        self._type = 'Bubble'
        self._namespace = 'dash_dthree_hooks'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'clicked', 'data', 'height', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Bubble, self).__init__(**args)
