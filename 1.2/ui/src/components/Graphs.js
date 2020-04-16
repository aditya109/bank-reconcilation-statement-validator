import React from 'react'
import ChordDiagram from 'react-chord-diagram'

const matrix = [
    [11975, 5871, 0, 2868],
    [1951, 10048, 2060, 0],
    [8010, 0, 8090, 8045],
    [1013, 990, 0, 6907]
];

export default class Graphs extends React.Component {
    constructor() {
        super()
        this.state = {

        }
    }
    render() {
        return (
            <div>
                <div className = "chord-graph-title-container">
                    <div className= "title-text">
                        ChordDiagram
                    </div>
                </div>
                <ChordDiagram
                    className = "graph-options"
                    matrix={matrix}
                    componentId={1}
                    groupLabels={['CPNC', 'CDA', 'Credit', 'Debit']}
                    groupColors={["#000000", "#FFDD89", "#957244", "#F26223"]}
                    
                />
            </div>
        )
    }
}