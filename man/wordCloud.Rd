% Auto-generated: do not edit by hand
\name{wordCloud}

\alias{wordCloud}

\title{WordCloud component}

\description{
WordCloud component using d3 and hooks
}

\usage{
wordCloud(id=NULL, clicked=NULL, clickedTimestamp=NULL, data=NULL,
selected=NULL, style=NULL, wrapperStyle=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{clicked}{Named list. Clicked word object (from d3)}

\item{clickedTimestamp}{Numeric. Clicked timestamp}

\item{data}{Unnamed list. Data}

\item{selected}{List of numerics. Array containing selected items
Defaults to empty array}

\item{style}{Named list. Chart style}

\item{wrapperStyle}{Named list. wrapper div style}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

