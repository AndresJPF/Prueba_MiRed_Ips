import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {
  User,
  UserCreate,
  UserUpdate,
  UserListResponse,
} from '../models/user.model';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class UserService {
  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient) {}

  getUsers(
    page: number = 1,
    pageSize: number = 10,
  ): Observable<UserListResponse> {
    return this.http.get<UserListResponse>(
      `${this.apiUrl}/users?page=${page}&page_size=${pageSize}`,
    );
  }

  getUser(id: number): Observable<User> {
    return this.http.get<User>(`${this.apiUrl}/users/${id}`);
  }

  createUser(data: UserCreate): Observable<User> {
    return this.http.post<User>(`${this.apiUrl}/users`, data);
  }

  updateUser(id: number, data: UserUpdate): Observable<User> {
    return this.http.put<User>(`${this.apiUrl}/users/${id}`, data);
  }

  deleteUser(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/users/${id}`);
  }
}
