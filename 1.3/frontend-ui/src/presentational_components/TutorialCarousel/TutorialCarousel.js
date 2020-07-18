import React from "react";
import "./tutorialcarousel.scss";
import { Carousel, Button, Modal } from "react-bootstrap";

function MyVerticallyCenteredModal(props) {
  return (
    <Modal
      {...props}
      size="lg"
      aria-labelledby="contained-modal-title-vcenter"
      centered
    >
      <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">
          Modal heading
        </Modal.Title>
      </Modal.Header>
      <Modal.Body>
        
      </Modal.Body>
      <Modal.Footer>
        <Button onClick={props.onHide}>Close</Button>
      </Modal.Footer>
    </Modal>
  );
}

function TutorialCarousel() {
  const [modalShow, setModalShow] = React.useState(false);

  return (
    <>
      <div className="get-started">
        <button onClick={() => setModalShow(true)} className="get-started-btn">
          <span>Get Started</span>
        </button>
      </div>

      <MyVerticallyCenteredModal
        show={modalShow}
        onHide={() => setModalShow(false)}
      />
    </>
  );
}

export default TutorialCarousel;
