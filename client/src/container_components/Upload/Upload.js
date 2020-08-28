import React from "react";
import "./upload.css";
import axios from "axios";

export default class Upload extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            file: null,
        };
        this.onFormSubmit = this.onFormSubmit.bind(this);
        this.onChange = this.onChange.bind(this);
        this.fileUpload = this.fileUpload.bind(this);
    }

    onFormSubmit(e) {
        e.preventDefault();
        // console.log(e.target.value);
        // this.fileUpload(this.state.file).then((response) => {
        //     console.log(response.data);
        // });
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

    render() {
        return (
            <div className="upload__section" id="upload">
                <form onSubmit={this.onFormSubmit}>
                    {/*Upload files using click-button*/}
                    <div className="click__upload">
                        <div className="upload__text">
                            <span>Please choose a file</span>
                        </div>
                        <div className="file__upload">
                            <input type="file" onChange={this.onChange}/>
                            <i className="fa fa-arrow-up"></i>
                        </div>
                    </div>

                    {/*OR*/}
                    <div className="or">
                        <span>OR</span>
                    </div>

                    {/*Upload files using drop zone*/}
                    <div className="drop__zone">
                        <div className="file__upload__wrap">
                            <input
                                className="file__upload__input"
                                type="file"
                                accept="file/*"
                            />
                            <div className="drag__text">
                                <h3>Drag and drop a file</h3>
                            </div>
                        </div>
                    </div>

                    {/*Submit Button*/}
                    <button className="submit__btn" type="submit">Upload</button>
                </form>
            </div>
        );
    }
}
