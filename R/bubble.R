# AUTO GENERATED FILE - DO NOT EDIT

bubble <- function(id=NULL, width=NULL, height=NULL, data=NULL, clicked=NULL) {
    
    props <- list(id=id, width=width, height=height, data=data, clicked=clicked)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Bubble',
        namespace = 'dash_dthree_hooks',
        propNames = c('id', 'width', 'height', 'data', 'clicked'),
        package = 'dashDthreeHooks'
        )

    structure(component, class = c('dash_component', 'list'))
}
