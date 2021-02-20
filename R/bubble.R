# AUTO GENERATED FILE - DO NOT EDIT

bubble <- function(id=NULL, label=NULL, value=NULL) {
    
    props <- list(id=id, label=label, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Bubble',
        namespace = 'dash_dthree_hooks',
        propNames = c('id', 'label', 'value'),
        package = 'dashDthreeHooks'
        )

    structure(component, class = c('dash_component', 'list'))
}
