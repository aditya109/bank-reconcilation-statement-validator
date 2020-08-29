import { initialFileState } from "./state";
import { UPDATE_FILE_STATUS} from "../actionTypes";

export const fileStateReducer = (state = initialFileState, action) => {
    switch (action.type) {
        case UPDATE_FILE_STATUS:
            return {
                ...state,
                file: action.payload
            };
        default:
            return state;
    }
};

