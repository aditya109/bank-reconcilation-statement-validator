import React from "react";
import "./card.css";

function Card(props) {
    console.log("Card Component loaded")

    return (
        <div className="card">

            {/*Card Header*/}

            <div className="card__header">
                <div className="title__text__head">
                    <span className="title__text">{props.title_head_short}</span>
                </div>
            </div>

            {/*Card Text*/}

            <div className="card__text">
                <span className="subtitle">{props.eta}</span>
                <h2>{props.title_head_full}</h2>
                <div className="table__data">
                    <table className="metadata__table">
                        <tbody>
                        <tr className="table__head__row">
                            <th className="table__head">Pre-Evaluation</th>
                        </tr>
                        </tbody>
                        <tbody>
                        <tr className="table__row">
                            <td className="col__1">Total Transactions:</td>
                            <td className="col__2">170000</td>
                        </tr>
                        </tbody>
                        <tbody>
                        <tr className="table__row">
                            <td className="col__1">Grand Total:</td>
                            <td className="col__2">
                                <span>&#8377;&nbsp; 340k</span>
                            </td>
                        </tr>
                        </tbody>
                        <tbody>
                        <tr className="table__head__row">
                            <th className="table__head">Post-Evaluation</th>
                        </tr>
                        </tbody>
                        <tbody>
                        <tr className="table__row">
                            <td className="col__1">Transactions:</td>
                            <td className="col__2">170000</td>
                        </tr>
                        </tbody>
                        <tbody>
                        <tr className="table__row">
                            <td className="col__1">Grand Total :</td>
                            <td className="col__2">
                                <span>&#8377; 340k </span>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            {/*Card Stats*/}

            <div className="card__stats">
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
