import React from "react";
import "./card.scss";

function Card(props) {
    console.log("Card Component loaded")

    return (
        <div className="card">
            <div className="card-image-1">
                <h1 className="title-text-head">
                    <span className="title-text">{props.title_head_short}</span>
                </h1>
            </div>
            <div className="card-text">
                <span className="subtitle">{props.eta}</span>
                <h2>{props.title_head_full}</h2>
                <div className="table-data">
                    <table className="metadata-table">
                        <tbody>
                        <tr className="table-head-row">
                            <th className="table-head">Pre-Evaluation</th>
                        </tr>
                        </tbody>
                        <tbody>
                        <tr className="table-row">
                            <td className="col-1">Total Transactions:</td>
                            <td className="col-2">170000</td>
                        </tr>
                        </tbody>
                        <tbody>
                        <tr className="table-row">
                            <td className="col-1">Grand Total:</td>
                            <td className="col-2">
                                <span>&#8377;&nbsp; 340k</span>
                            </td>
                        </tr>
                        </tbody>
                        <tbody>
                        <tr className="table-head-row">
                            <th className="table-head">Post-Evaluation</th>
                        </tr>
                        </tbody>
                        <tbody>
                        <tr className="table-row">
                            <td className="col-1">Transactions:</td>
                            <td className="col-2">170000</td>
                        </tr>
                        </tbody>
                        <tbody>
                        <tr className="table-row">
                            <td className="col-1">Grand Total :</td>
                            <td className="col-2">
                                <span>&#8377; 340k </span>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <div className="card-stats">
                <div className="stat">
                    <div className="value">&#8377; 3 lakh</div>
                    <div className="type">Cash Found</div>
                </div>

                <div className="stat">
                    <div className="value">&#8377; 34 k</div>
                    <div className="type">Cash Not Found</div>
                </div>
            </div>
        </div>
    );
}

export default Card;
