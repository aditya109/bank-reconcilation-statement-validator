import React from "react";

import "../styles/css/components/disclaimer_content.css";

function DisclaimerContent() {
  return (
    <div className="warning-text-div">
      <span className="warning-text-high">
        This is to inform you as an end-user that this application is in
        alpha-phase and is meant for automating the laborious work done to
        detect erroneous transactions done manually. So it is an earnest request
        to bear with simple-minded UI or noticeable server-response latencies,
        since the focus majored on the use-cases and not on the UI. This
        application is not supposed to be hosted on net unless approved by Dev.
        Please do not try to tamper with the code or induce malicious code in
        any manner.
      </span>
    </div>
  );
}

export default DisclaimerContent;
