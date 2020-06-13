import React, { useState } from "react";
import Modal from "react-bootstrap/Modal";
import Button from "react-bootstrap/Button";

import "../styles/css/components/disclaimer_content.css";

const TModal = (props) => {
  const [show, setShow] = useState(false);
  return (
    <div>
      <Button variant={props.attribute.variant} onClick={() => setShow(true)}>
        {props.attribute.button_text}
      </Button>
      <Modal
        show={show}
        onHide={() => setShow(false)}
        dialogClassName="modal-90w"
        aria-labelledby="example-custom-modal-styling-title"
        centered="true"
      >
        <Modal.Header closeButton>
          <Modal.Title id="example-custom-modal-styling-title">
            {props.attribute.modal_title}
          </Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <span>{props.attribute.component}</span>
        </Modal.Body>
      </Modal>
    </div>
  );
};

export default class CustomModal extends React.Component {
  render() {
    return <TModal attribute={this.props} />;
  }
}
