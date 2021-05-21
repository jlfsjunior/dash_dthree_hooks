# AUTO GENERATED FILE - DO NOT EDIT

export wordcloud

"""
    wordcloud(;kwargs...)

A WordCloud component.
WordCloud component using d3 and hooks
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `clicked` (Dict; optional): Clicked word object (from d3)
- `clickedTimestamp` (Real; optional): Clicked timestamp
- `data` (Array; optional): Data
- `selected` (Array of Reals; optional): Array containing selected items
Defaults to empty array
- `style` (Dict; optional): Chart style
- `wrapperStyle` (Dict; optional): wrapper div style
"""
function wordcloud(; kwargs...)
        available_props = Symbol[:id, :clicked, :clickedTimestamp, :data, :selected, :style, :wrapperStyle]
        wild_props = Symbol[]
        return Component("wordcloud", "WordCloud", "dash_dthree_hooks", available_props, wild_props; kwargs...)
end

