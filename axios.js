/* eslint-disable no-underscore-dangle */
// config.headers["Authorization"] =
// "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJfNDZBcGhPTVc5LW1GWnhOaVpFSEZZTUlvZEVaMXVxb0JnS0hRQVZzNVhjIn0.eyJqdGkiOiIwMjliMGFiYy0wMjU3LTRjZmEtOTkxYS02ZDNkMTk4ZTU3MjUiLCJleHAiOjE4NzY0NTk4NDcsIm5iZiI6MCwiaWF0IjoxNTYxMDk5ODQ3LCJpc3MiOiJodHRwczovL2F1dGhtYWZ0c3QuYXZpdmFzYS5jb20udHIvYXV0aC9yZWFsbXMvaW50ZXJuYWwiLCJhdWQiOiJiYXNpYyIsInN1YiI6IjcwMzk1ZDk2LWUyOGQtNDM5OS04NmQzLTRlMWIxZDNhYmE4NiIsInR5cCI6IkJlYXJlciIsImF6cCI6ImJhc2ljIiwiYXV0aF90aW1lIjowLCJzZXNzaW9uX3N0YXRlIjoiYzRlNDYxNDYtYmIyOS00NWQwLWI3YjAtYTc4MjAxYWEzZTcyIiwiYWNyIjoiMSIsImNsaWVudF9zZXNzaW9uIjoiMWZjYjgwZjQtNmNhOC00ZGE1LWE0OTctZmZkYzI1NzQyYTQyIiwiYWxsb3dlZC1vcmlnaW5zIjpbXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIk1vZHVsZVNhbGVzIiwiTW9kdWxlQ29udGVudCIsIk1vZHVsZVpla2FLdXB1IiwiTW9kdWxlQWRtaW4iLCJNb2R1bGVDb3JwIiwidW1hX2F1dGhvcml6YXRpb24iLCJNb2R1bGVPcGVyYXRpb25hbCJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJ2aWV3LXByb2ZpbGUiXX19LCJuYW1lIjoiIiwicHJlZmVycmVkX3VzZXJuYW1lIjoic3dhZ2dlciJ9.mthwklCE79OwIwKWPp16uGG8BUWMZiBY3nsCWG37P_mKzb75AMCrRXiGTUIAnmMKkwtbbCFaQdMhxyfCU0_Kyalgc7CYXGgidfPKPigvRL84sFYSq9Y7QA8MQTuqBc68gudxIN4mbRlprFaSzRhLJH0PJe8TrsWt3-6k7XdGhrPUQMlBW_wD_U0jz6FsdUJUvUVMr0yIZGXex9Mr2rw-nRfvhXfbiTv1XsZdmlpt5Yt4CqO2fCRfjv4bmMMkrfayjpqzzWle_eRk7dNRmqBbPFHlBNmhBDbAtYJPK0PMWB08Yj5l6uKPB7k1PeeecySvLDCaGJT8L6r2GwBsRSvjOg"
// config.headers["x-auth-config"] = "internal"

import axios from 'axios'
import loginState from '@avivasa/redux/states/login'
import { store } from '@avivasa/webcore'
import getJsSessionId from './SessionUUID'
import loaderState from '@avivasa/redux/states/loader'
import apiErrorPopupState from '@avivasa/redux/states/apiError'

const httpAuthorizationErrorCode = 401
const httpForbiddenErrorCode = 403
const httpValidationCode = 400

const setupAxiosInterceptors = () => {
  const onRequestSuccess = config => {
    loaderState.increaseCallCount()
    const loginState = store.getState().loginState
    if (loginState && loginState.isAuthenticated && !config.url.includes('/login')) {
      config.headers['Token'] = loginState.access_token
      config.headers['Content-Type'] = 'application/json; charset=UTF-8'
      config.headers['jss'] = getJsSessionId()
      config.headers['X-applicationId'] = 'indexcenter'
    }
    // istemedigimiz durumda gostermemek icin
    if (!config.dontShowLoader) {
      if (!loaderState.getState().isLoaderVisible) {
        loaderState.showLoader()
      }
    }
    config.timeout = 300000
    return config
  }
  const onResponseSuccess = response => {
    loaderState.decreaseCallCount()
    if (loaderState.getState().callCount === 0 && loaderState.getState().isLoaderVisible) {
      loaderState.hideLoader()
    }
    return response
  }

  const onResponseError = error => {
    loaderState.decreaseCallCount()
    let statusCode = error.response ? error.response.status : 0
    if (statusCode == httpForbiddenErrorCode && process.env.NODE_ENV != 'development') {
      if (store.getState().loginState.isAuthenticated) {
        loginState.logout().then(response => {
          if (response) {
            window.location.replace(response.url)
          }
        })
      }
    } else if (statusCode == httpAuthorizationErrorCode && process.env.NODE_ENV != 'development') {
      if (store.getState().loginState.isAuthenticated) {
        loginState.logout().then(response => {
          if (response) {
            window.location.replace(response.url)
          }
        })
      }
    } else if (statusCode !== httpValidationCode && !error.config.dontShowErrorWarning) {
      apiErrorPopupState.showApiErrorPopup()
    }
    if (loaderState.getState().callCount === 0 && loaderState.getState().isLoaderVisible) {
      loaderState.hideLoader()
    }
    return Promise.reject(error.response.data)
  }

  axios.interceptors.request.use(onRequestSuccess)
  axios.interceptors.response.use(onResponseSuccess, onResponseError)
}
export default setupAxiosInterceptors
