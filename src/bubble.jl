# AUTO GENERATED FILE - DO NOT EDIT

export bubble

"""
    bubble(;kwargs...)

A Bubble component.
Bubble component using d3 and hooks
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `width` (Real; optional): Chart width
- `height` (Real; optional): Chart height
- `data` (Array; optional): Data
"""
function bubble(; kwargs...)
        available_props = Symbol[:id, :width, :height, :data]
        wild_props = Symbol[]
        return Component("bubble", "Bubble", "dash_dthree_hooks", available_props, wild_props; kwargs...)
end

