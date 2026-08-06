import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, tap } from 'rxjs';
import {
  LoginRequest,
  RegisterRequest,
  TokenResponse,
} from '../models/auth.model';
import { User } from '../models/user.model';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient) {}

  login(data: LoginRequest): Observable<TokenResponse> {
    return this.http
      .post<TokenResponse>(`${this.apiUrl}/auth/login`, data)
      .pipe(
        tap((response) => {
          localStorage.setItem('token', response.access_token);
        }),
      );
  }

  register(data: RegisterRequest): Observable<User> {
    return this.http.post<User>(`${this.apiUrl}/auth/register`, data);
  }

  logout(): Observable<any> {
    return this.http.post(`${this.apiUrl}/auth/logout`, {});
  }

  getMe(): Observable<User> {
    return this.http.get<User>(`${this.apiUrl}/auth/me`);
  }

  getToken(): string | null {
    return localStorage.getItem('token');
  }

  isAuthenticated(): boolean {
    return !!this.getToken();
  }

  removeToken(): void {
    localStorage.removeItem('token');
  }
}
