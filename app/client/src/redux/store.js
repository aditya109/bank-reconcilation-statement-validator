import {createStore} from 'redux';
import {updateFileStatus} from "./actions";

const store = createStore(updateFileStatus);

export default store;