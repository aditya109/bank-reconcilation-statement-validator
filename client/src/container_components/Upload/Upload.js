import React from "react";
import "./upload.scss";
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
    console.log(e.target.value);
    this.fileUpload(this.state.file).then((response) => {
      console.log(response.data);
    });
  }
  onChange(e) {
    this.setState({ file: e.target.files[0] });
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
      <section className="upload-section" id="upload">
        <form onSubmit={this.onFormSubmit}>
          <div className="click-upload">
            <div className="upload-text">
              <span>Please choose a file</span>
            </div>
            <div className="file-upload">
              <input type="file" onChange={this.onChange} />
              <i className="fa fa-arrow-up"></i>
            </div>
          </div>
          <div className="or">
            <span>OR</span>
          </div>
          <div className="drop-zone">
            <div className="file-upload-wrap">
              <input
                className="file-upload-input"
                type="file"
                accept="file/*"
              />
              <div className="drag-text">
                <h3>Drag and drop a file</h3>
              </div>
            </div>
            <div className="file-upload-content">
              <div className="file-title-wrap">
                <button type="button" className="remove-file">
                  Remove <span className="file-title">Uploaded File</span>
                </button>
              </div>
            </div>
          </div>
          <button className="submit-btn" type="submit">Upload</button>
          {/* <div className="upload-progress">
          <div className="container-2">
            <div className="btn btn-two">
              <span>UPLOAD</span>
            </div>
          </div>
          <div className="progress-bar-div">
            <div className="progress">
              <div className="progress-value"></div>
            </div>
          </div>
        </div> */}
        </form>
      </section>
    );
  }
}
