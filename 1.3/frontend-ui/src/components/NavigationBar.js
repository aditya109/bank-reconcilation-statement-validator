import React from 'react'
import * as ReactBootStrap from "react-bootstrap";
import NavDropdown from "react-bootstrap/NavDropdown";

import "../styles/css/components/navigationbar.css";

function NavigationBar() {
    return (
        <div className="navigation-bar-container">
          <ReactBootStrap.Navbar
            collapseOnSelect
            expand="sm"
            variant="light"
            fixed="bottom"
            className="navbar-custom"
          >
            <ReactBootStrap.Navbar.Brand className="nav-title" href="#home">
              BRSV
            </ReactBootStrap.Navbar.Brand>
            <ReactBootStrap.Navbar.Toggle aria-controls="responsive-navbar-nav" />
            <ReactBootStrap.Navbar.Collapse id="responsive-navbar-nav">
              <ReactBootStrap.Nav className="mr-auto">
                <ReactBootStrap.Nav.Link href="tutorials">
                  Tutorials
                </ReactBootStrap.Nav.Link>
                <ReactBootStrap.Nav.Link href="#pricing"></ReactBootStrap.Nav.Link>
                
              </ReactBootStrap.Nav>
              <ReactBootStrap.Nav>
                <ReactBootStrap.Nav.Link href="history">
                  History
                </ReactBootStrap.Nav.Link>
              </ReactBootStrap.Nav>
            </ReactBootStrap.Navbar.Collapse>
          </ReactBootStrap.Navbar>
        </div>
    )
}
export default NavigationBar;