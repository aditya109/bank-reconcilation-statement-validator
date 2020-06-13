import React from 'react'

export default class WarningPage extends React.Component {
    constructor() {
        super()

    }
    render() {
        return (
            <div>
                <div className="warning-title-container">
                    <div className="title-text">
                        Warning !!
                    </div>
                </div>
                <div className="warning-content">
                    <div className="warning-text-white">
                        Please take note the once the redundancy mechanism is triggered,&nbsp;
                    </div>
                    <div className="warning-text-red">
                        <u>the redundant records will be removed</u>.
                    </div>
                    <div className="warning-text-white">
                        So pay heed before proceeding to search the dataframes, as&nbsp;
                    </div>
                    <div className="warning-text-red">
                        <u>the search jobs CAN be stopped, but NOT reversed !</u>
                    </div>
                </div>
                <div className="nav-button-div">
                    <div className="go-back-btn" align="center">
                        <span>Go Back To Previous Page</span>
                    </div>

                    <div class="continue-btn" align="center" onClick={(e) => { this.handleChecked(e) }}>
                        <span>continue</span>
                    </div>
                </div>

            </div>
        )
    }
}