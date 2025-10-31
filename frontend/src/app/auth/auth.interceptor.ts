import { HttpInterceptorFn } from '@angular/common/http';

const TOKEN_KEY = 'auth_token'; 

export const authInterceptor: HttpInterceptorFn = (req, next) => {
  
  const authToken = localStorage.getItem(TOKEN_KEY); 

  if (authToken) {
    const authReq = req.clone({
      setHeaders: {
        Authorization: `Token ${authToken}` 
      }
    });
    return next(authReq);
  }

  return next(req);
};