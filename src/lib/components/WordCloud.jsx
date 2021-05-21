import {useRef, useEffect} from 'react';
import PropTypes from 'prop-types';

import {useResizeObserver} from '../helpers/Hooks.jsx';

// Inspired by
//  https://github.com/Yoctol/react-d3-cloud/blob/master/README.md
import cloud from 'd3-cloud';
import * as d3 from 'd3';

// FIXME: Add deep copy library to allow deep object
const defaultStyle = {
    padding: 5,
    fillRegular: 'black',
    fillHover: 'gray',
    fillSelected: 'red',
    fontFamily: 'Cera Pro, Noto Sans',
    fontSizeMin: 16,
    fontSizeMax: 40,
    fontSizeScale: 'linear', // log or sqrt
    transitionDuration: 500,
};

/**
 * WordCloud component using d3 and hooks
 */
const WordCloud = ({
    id,
    setProps,
    data,
    clicked,
    clickedTimestamp,
    selected,
    style,
    wrapperStyle,
}) => {
    const svgRef = useRef(null);
    const wrapperRef = useRef(null);
    const dimensions = useResizeObserver(wrapperRef);

    // TODO use hooks to update selected

    useEffect(() => {
        if (!data || !svgRef.current || !dimensions) return;

        const svg = d3.select(svgRef.current);

        const words_g = svg
            .select('g.wordsLayer')
            .attr(
                'transform',
                `translate(${dimensions.width / 2},${dimensions.height / 2})`
            );

        // Style definitions
        const chartStyle = {...defaultStyle, ...style};

        const fill = d3.scaleOrdinal(d3.schemeCategory10);

        const getFill = (word) => {
            if (!selected) return chartStyle.fillRegular;

            return selected.includes(word.id)
                ? chartStyle.fillSelected
                : chartStyle.fillRegular;
        };

        const fontScaleChoices = {
            linear: d3.scaleLinear(),
            log: d3.scaleLog(),
            sqrt: d3.scaleSqrt(),
        };

        const fontScale = fontScaleChoices[chartStyle.fontSizeScale || 'linear']
            .domain(d3.extent(data, (d) => d.value))
            .range([chartStyle.fontSizeMin, chartStyle.fontSizeMax]);

        const rotate = (word) => 0; //  word.value % 360;

        const t = d3.transition().duration(chartStyle.transitionDuration);

        const layout = cloud()
            .size([dimensions.width, dimensions.height])
            .words(data)
            .font(chartStyle.fontFamily)
            .padding(chartStyle.padding)
            .rotate(rotate)
            .random((val) => 1)
            .fontSize((word) => fontScale(word.value))
            .on('end', (words) => {
                const texts = words_g
                    .selectAll('text')
                    .data(words, (d) => d.id);

                texts
                    .exit()
                    .transition(t)
                    .style('font-size', (d) => 0)
                    .remove();

                texts
                    .attr(
                        'transform',
                        (d) => `translate(${[d.x, d.y]})rotate(${d.rotate})`
                    )
                    .style('fill', getFill)
                    .on('mouseover', (event, word) => {
                        d3.select(event.currentTarget).style(
                            'fill',
                            chartStyle.fillHover
                        );
                    })
                    .on('mouseout', (event, word) => {
                        d3.select(event.currentTarget).style('fill', getFill);
                    });

                texts
                    .enter()
                    .append('text')
                    .style('font-family', 'Cera Pro')
                    // .style('fill', (d, i) => fill(i))
                    .style('fill', getFill)
                    .attr('text-anchor', 'middle')
                    .style('cursor', 'pointer')
                    .style('user-select', 'none')
                    .attr(
                        'transform',
                        (d) => `translate(${[d.x, d.y]})rotate(${d.rotate})`
                    )
                    .text((d) => d.text)
                    .style('font-size', 0)
                    // events
                    .on('mouseover', (event, word) => {
                        d3.select(event.currentTarget).style(
                            'fill',
                            chartStyle.fillHover
                        );
                    })
                    .on('mouseout', (event, word) => {
                        d3.select(event.currentTarget).style('fill', getFill);
                    })
                    .on('click', (event, word) => {
                        // setProps({clicked: word});
                        setProps({clicked: word, clickedTimestamp: Date.now()});

                        // console.log(selected);

                        // if (selected.includes(id)) {
                        //     const newSelected = selected.filter(
                        //         (item) => item !== id
                        //     );

                        //     console.log(newSelected);

                        //     setProps({selected: newSelected});
                        //     setProps({clicked: word});
                        //     // setSel(selected.filter((item) => item !== id));
                        //     // console.log(newSelection);
                        // } else {
                        //     selected.push(id);

                        //     const newSelected = [...selected];
                        //     console.log(newSelected);
                        //     setProps({selected: newSelected});

                        //     // setSel(selected);
                        // }

                        // d3.select(event.currentTarget).style('fill', getFill);
                    })
                    // transition
                    .transition(t)
                    .style('font-size', (d) => `${d.size}px`);
            });

        layout.start();
    }, [data, dimensions, selected]);

    return (
        <div
            id={id}
            ref={wrapperRef}
            style={{
                ...{width: '100%', height: '50vh', margin: '0 auto'},
                ...wrapperStyle,
            }}
        >
            <svg ref={svgRef} style={{width: '100%', height: '100%'}}>
                <g className={'wordsLayer'} />
            </svg>
        </div>
    );
};

WordCloud.defaultProps = {
    selected: [],
    style: defaultStyle,
};

WordCloud.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,

    /** Data */
    data: PropTypes.array,

    /**
     * Clicked word object (from d3)
     */
    clicked: PropTypes.object,

    /**
     * Clicked timestamp
     */
    clickedTimestamp: PropTypes.number,

    /**
     * Array containing selected items
     * Defaults to empty array
     */
    selected: PropTypes.arrayOf(PropTypes.number),

    /**
     * Chart style
     */
    style: PropTypes.object,

    /**
     * wrapper div style
     */
    wrapperStyle: PropTypes.object,
};

export default WordCloud;
