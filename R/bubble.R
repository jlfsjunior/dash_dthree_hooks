# AUTO GENERATED FILE - DO NOT EDIT

bubble <- function(id=NULL, clicked=NULL, data=NULL, height=NULL, width=NULL) {
    
    props <- list(id=id, clicked=clicked, data=data, height=height, width=width)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Bubble',
        namespace = 'dash_dthree_hooks',
        propNames = c('id', 'clicked', 'data', 'height', 'width'),
        package = 'dashDthreeHooks'
        )

    structure(component, class = c('dash_component', 'list'))
}
