# AUTO GENERATED FILE - DO NOT EDIT

wordCloud <- function(id=NULL, clicked=NULL, clickedTimestamp=NULL, data=NULL, selected=NULL, style=NULL, wrapperStyle=NULL) {
    
    props <- list(id=id, clicked=clicked, clickedTimestamp=clickedTimestamp, data=data, selected=selected, style=style, wrapperStyle=wrapperStyle)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'WordCloud',
        namespace = 'dash_dthree_hooks',
        propNames = c('id', 'clicked', 'clickedTimestamp', 'data', 'selected', 'style', 'wrapperStyle'),
        package = 'dashDthreeHooks'
        )

    structure(component, class = c('dash_component', 'list'))
}
