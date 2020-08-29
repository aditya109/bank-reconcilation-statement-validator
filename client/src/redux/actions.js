import {FETCH_BRS_RESULTS, UPDATE_FILE_STATUS} from "./reducers/actionTypes";

function updateFileStatus(file) {
    console.log("This is working... action!")
    console.log(file)
    return {
        type: UPDATE_FILE_STATUS,
        payload: file,
    };
}

function fetchBRSResults() {
    return {
        type: FETCH_BRS_RESULTS
    };
}

export {
    updateFileStatus,
    fetchBRSResults
};