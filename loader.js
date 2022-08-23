import { State } from '@avivasa/webcore'

const loaderState = State({
  name: 'loaderState',
  initial: {
    isLoaderVisible: false,
    callCount: 0
  },
  showLoader: function() {
    return { isLoaderVisible: true }
  },
  hideLoader: function() {
    return { isLoaderVisible: false }
  },
  increaseCallCount: function() {
    return { callCount: ++this.state.callCount }
  },
  decreaseCallCount: function() {
    return { callCount: --this.state.callCount }
  }
})
export default loaderState
