import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {
  Product,
  ProductCreate,
  ProductUpdate,
  ProductListResponse,
} from '../models/product.model';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class ProductService {
  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient) {}

  getProducts(
    page: number = 1,
    pageSize: number = 10,
    categoriaId?: number,
    estado?: string,
  ): Observable<ProductListResponse> {
    let url = `${this.apiUrl}/productos?page=${page}&page_size=${pageSize}`;
    if (categoriaId) url += `&categoria_id=${categoriaId}`;
    if (estado) url += `&estado=${estado}`;
    return this.http.get<ProductListResponse>(url);
  }

  getProduct(id: number): Observable<Product> {
    return this.http.get<Product>(`${this.apiUrl}/productos/${id}`);
  }

  createProduct(data: ProductCreate): Observable<Product> {
    return this.http.post<Product>(`${this.apiUrl}/productos`, data);
  }

  updateProduct(id: number, data: ProductUpdate): Observable<Product> {
    return this.http.put<Product>(`${this.apiUrl}/productos/${id}`, data);
  }

  deleteProduct(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/productos/${id}`);
  }
}
