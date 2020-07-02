import React from "react";
import "./styles/upload.scss";

function Upload() {
  return (
    <section className="upload-section">
      <div className="click-upload">
        <div className="upload-text">
          <span>Please choose a file</span>
        </div>
        <div className="file-upload">
          <input type="file" />
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
            onchange="readURL(this);"
            accept="file/*"
          />
          <div className="drag-text">
            <h3>Drag and drop a file</h3>
          </div>
        </div>
        <div className="file-upload-content">
          <div className="file-title-wrap">
            <button type="button" onclick="removeUpload()" className="remove-file">
              Remove <span className="file-title">Uploaded File</span>
            </button>
          </div>
        </div>
      </div>
      <div className="upload-progress">
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
      </div>
    </section>
  );
}

export default Upload;
