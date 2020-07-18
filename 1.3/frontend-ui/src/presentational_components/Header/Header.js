import React from "react";
import "./header.css";

import { Navbar, Nav} from "react-bootstrap";

function Header() {
  console.log("Header Component loaded");
  return (
    
    <div className="navbar-container">
      <Navbar collapseOnSelect expand="lg" >
      {/* <Navbar collapseOnSelect > */}
        <Navbar.Brand className="brand" href="#home">BRSV</Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="ml-auto">
            <Nav.Link className="link" href="#features">Uploads</Nav.Link>
            <Nav.Link className="link" href="#features">Results</Nav.Link>
            <Nav.Link className="link" href="#features">Login/SignUp</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    </div>
  );
}

export default React.memo(Header);
