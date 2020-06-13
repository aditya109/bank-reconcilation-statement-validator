import React from "react";
import { Tab, Tabs, TabList, TabPanel } from "react-tabs";
import "react-tabs/style/react-tabs.css";

class PanelContent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <div>
        <div className="input-panel-container">
          <div className="panel-title-container">
            <div className="panel-title">
              <span className="panel-title-text">
                {this.props.tabIndex == 0
                  ? "Cheques Paid In But Not Credited (CPNC)"
                  : this.props.tabIndex == 1
                  ? "Credit (Cr)"
                  : this.props.tabIndex == 2
                  ? "Debit (Dr)"
                  : "Cheques Dishonor Action (CDA)"}
              </span>
            </div>
            <div className="panel-content">
              <div className="input-div">
                <div className="input-1">
                  <span className="column-input-text">
                    Enter the columnar data for Transaction Dates
                  </span>
                  <div className="input-text-area">
                    <textarea
                      placeholder="transaction-dates only"
                      id="w3mission"
                      rows="6"
                      cols="115"
                    ></textarea>
                  </div>
                </div>
                <div className="input-1">
                  <span className="column-input-text">
                    Enter the columnar data for Cheques Information
                  </span>
                  <div className="input-text-area">
                    <textarea
                      id="w3mission"
                      rows="6"
                      cols="115"
                      placeholder="cheques-numbers only"
                    ></textarea>
                  </div>
                </div>
                <div className="input-1">
                  <span className="column-input-text">
                    Enter the columnar data for Transaction Amount
                  </span>
                  <div className="input-text-area">
                    <textarea
                      id="w3mission"
                      rows="6"
                      cols="115"
                      placeholder="transaction-amounts only "
                    ></textarea>
                  </div>
                </div>
              </div>
              <div className="btn-div">
                <div className="load-btn" align="center">
                  <span>Load Up Data &#8686;</span>
                </div>
                <div
                  class="nav-btn"
                  align="right"
                  onClick={(e) => {
                    this.handleChecked(e);
                  }}
                >
                  <span>Navigate to Search Operations</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

class DFLoadingPage extends React.Component {
  constructor() {
    super();
    this.state = {
      tabIndex: 0,
    };
  }

  render() {
    return (
      <div className="nav-page-container">
        <div className="nav-page-title-div">
          <div className="nav-page-title-text">
            <span className="title-text">Data Frame Loader</span>
          </div>
        </div>
        <div className="tabs-panel-container">
          <Tabs
            selectedIndex={this.state.tabIndex}
            onSelect={(tabIndex) => this.setState({ tabIndex })}
            selectedTabClassName="sel-tab"
            disabledTabClassName="dis-tab"
          >
            <TabList>
              <Tab>Cheques Paid In But Not Credited (CPNC)</Tab>
              <Tab>Credit (Cr)</Tab>
              <Tab>Debit (Dr)</Tab>
              <Tab>Cheque Dishonor Action (CDA)</Tab>
            </TabList>
            <TabPanel>
              <PanelContent tabIndex={this.state.tabIndex} />
            </TabPanel>
            <TabPanel>
              <PanelContent tabIndex={this.state.tabIndex} />
            </TabPanel>
            <TabPanel>
              <PanelContent tabIndex={this.state.tabIndex} />
            </TabPanel>
            <TabPanel>
              <PanelContent tabIndex={this.state.tabIndex} />
            </TabPanel>
          </Tabs>
        </div>
      </div>
    );
  }
}
export default DFLoadingPage;
