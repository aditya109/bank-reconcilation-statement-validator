import React, { useState } from "react";
import * as ReactBoostStrap from "react-bootstrap";
import Button from "react-bootstrap/Button";

import "../styles/css/components/custom_modal.css";

const TModal = (props) => {
  const [show, setShow] = useState(false);
  return (
    <div className="parent-modal-container">
      <div className="view-widget-container">
        <ReactBoostStrap.InputGroup className="mb-4">
          <ReactBoostStrap.Button
            variant={props.attribute.variant}
            onClick={() => setShow(true)}
            size="lg"
          >
            {props.attribute.button_text}
          </ReactBoostStrap.Button>
        </ReactBoostStrap.InputGroup>
      </div>
      <ReactBoostStrap.Modal
        show={show}
        onHide={() => setShow(false)}
        dialogClassName="modal-90w"
        aria-labelledby="example-custom-modal-styling-title"
        centered="true"
        size="xl"
      >
        <ReactBoostStrap.Modal.Header closeButton>
          <ReactBoostStrap.Modal.Title id="example-custom-modal-styling-title">
            {props.attribute.modal_title}
          </ReactBoostStrap.Modal.Title>
        </ReactBoostStrap.Modal.Header>
        <ReactBoostStrap.Modal.Body>
          <p>{props.attribute.component}</p>
        </ReactBoostStrap.Modal.Body>
      </ReactBoostStrap.Modal>
    </div>
  );
};

export default class CustomModal extends React.Component {
  render() {
    return <TModal attribute={this.props} />;
  }
}
