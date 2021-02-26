import { useRef, useEffect } from 'react';
import PropTypes from 'prop-types';

import { useResizeObserver } from '../helpers/Hooks.jsx'

import * as d3 from 'd3';

/**
 * Bubble component using d3 and hooks
 */
const Bubble = ({id, width, height, data}) => {
    
    const svgRef = useRef(null);
    const wrapperRef = useRef(null);
    const dimensions = useResizeObserver(wrapperRef);

    useEffect(() => {

      if (!data || !svgRef.current || !dimensions) return;

      console.log(dimensions)

      const svg = d3.select(svgRef.current)

      const pointsG = svg.select("g.pointsLayer")

      // Chart properties
      const transitionDuration = 1000
      const [minRadius, maxRadius] = [1, 50]

      // Scales
      const xScale = d3.scaleLinear()
        .domain([0, d3.max(data, d => d.x)])
        .range([maxRadius, dimensions.width - maxRadius])

      const yScale = d3.scaleLinear()
        .domain([0, d3.max(data, d => d.y)])
        .range([dimensions.height - maxRadius, maxRadius])

      const rScale = d3.scaleLinear()
        .domain(d3.extent(data, d => d.r))
        .range([minRadius, maxRadius])

      // Data join
      const points = pointsG.selectAll("circle").data(data, d => d.id)

      points.exit()
        .transition()
          .duration(transitionDuration)
          .attr("r", d => 0)
        .remove()

      points
        .transition()
        .duration(transitionDuration)
        .attr("r", d => rScale(d.r))
        .attr("cx", d => xScale(d.x))
        .attr("cy", d => yScale(d.y))
        .attr("fill", d => d.color)

      points.enter()
        .append("circle")
        .attr("r", d => 0)
        .attr("cx", d => xScale(d.x))
        .attr("cy", d => yScale(d.y))
        .attr("fill", d => d.color)
        .transition()
          .duration(transitionDuration)
          .attr("r", d => rScale(d.r))

    }, [data, dimensions])
    
    
    return(
      <div id={id} ref={wrapperRef} style={{width: "100%", height: "50vh", margin: "0 auto"}}>
        <svg ref={svgRef} style={{width: "100%", height: "100%"}}>
          <g className={"pointsLayer"} />
        </svg>
      </div>
    )
}

export default Bubble;

Bubble.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,

    /** Chart width */
    width: PropTypes.number,

    /** Chart height */
    height: PropTypes.number,

    /** Data */
    data: PropTypes.array,

};
