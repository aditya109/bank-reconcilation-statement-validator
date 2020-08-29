import React from "react";
import "./upload.css";
import axios from "axios";
import {connect} from "react-redux";
import {updateFileStatus} from "../../redux/actions";

class Upload extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            file: null
        };
        this.onFormSubmit = this.onFormSubmit.bind(this);
        this.onChange = this.onChange.bind(this);
        this.fileUpload = this.fileUpload.bind(this);
        this.resetHandler = this.resetHandler.bind(this);
    }

    onFormSubmit(e) {
        e.preventDefault();
        console.log("This is working ... onFormSubmit")
        this.props.updateFileStatus(this.state.file);
    }

    onChange(e) {
        this.setState({file: e.target.files[0]});

    }

    fileUpload(file) {
        const formData = new FormData();
        formData.append("excel", file);
        axios
            .post(`http://localhost:5000/upload`, formData, {
                headers: {
                    "content-type": "multipart/form-data",
                },
            })
            .then(function () {
                console.log("SUCCESS !");
            })
            .catch(function () {
                console.log("FAILURE !");
            });
    }

    resetHandler = () => {
        this.setState({file: null})
    }

    render() {
        return (
            <div className="upload__section" id="upload">
                <form onSubmit={this.onFormSubmit}>
                    {/*Upload files using click-button*/}
                    <div className="click__upload">
                        <div className="upload__text">
                            {
                                this.state.file ? (
                                    <span>Click</span>
                                ) : (
                                    <span>Please choose a file</span>
                                )
                            }

                        </div>
                        <div className="file__upload">
                            <input type="file" onChange={this.onChange}/>
                            {
                                this.state.file ? (
                                    <i className="far fa-hand-point-down"/>
                                ) : (
                                    <i className="fa fa-arrow-up"/>
                                )
                            }
                        </div>
                    </div>

                    {/*Submit Button*/}
                    <div className="submit__btn__container">
                        <button className="submit__btn" type="submit">Upload <i className="fas fa-upload"/></button>
                        <span className="reset__btn" onClick={this.resetHandler}>Reset <i className="fas fa-redo-alt"/></span>

                    </div>
                </form>
            </div>
        );
    }
}

const mapStateToProps = state => {
    return {
        file: state.file
    }
}

const mapDispatchToProps = dispatch => {
    return {
        updateFileStatus: (file) => dispatch(updateFileStatus(file))
    }
}


export default connect(mapStateToProps, mapDispatchToProps)(Upload);
