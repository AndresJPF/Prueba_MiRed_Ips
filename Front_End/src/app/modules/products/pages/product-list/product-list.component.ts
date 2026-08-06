import { Component, OnInit } from '@angular/core';
import { Product } from '../../../../core/models/product.model';
import { Category } from '../../../../core/models/category.model';
import { ProductService } from '../../../../core/services/product.service';
import { CategoryService } from '../../../../core/services/category.service';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css'],
})
export class ProductListComponent implements OnInit {
  products: Product[] = [];
  categories: Category[] = [];
  loading = false;
  error = '';
  currentPage = 1;
  pageSize = 10;
  total = 0;
  filterCategory: number | null = null;
  filterEstado: string | null = null;

  constructor(
    private productService: ProductService,
    private categoryService: CategoryService,
  ) {}

  ngOnInit(): void {
    this.loadCategories();
    this.loadProducts();
  }

  loadCategories(): void {
    this.categoryService.getCategories().subscribe({
      next: (categories) => {
        this.categories = categories;
      },
      error: (err) => {
        console.error('Error al cargar categorías:', err);
      },
    });
  }

  loadProducts(): void {
    this.loading = true;
    this.error = '';
    this.productService
      .getProducts(
        this.currentPage,
        this.pageSize,
        this.filterCategory || undefined,
        this.filterEstado || undefined,
      )
      .subscribe({
        next: (response) => {
          this.products = response.data;
          this.total = response.total;
          this.loading = false;
        },
        error: (err) => {
          this.error = 'Error al cargar los productos';
          this.loading = false;
          console.error(err);
        },
      });
  }

  deleteProduct(id: number): void {
    if (!confirm('¿Estás seguro de eliminar este producto?')) return;
    this.productService.deleteProduct(id).subscribe({
      next: () => {
        this.loadProducts();
      },
      error: (err) => {
        this.error = 'Error al eliminar el producto';
        console.error(err);
      },
    });
  }

  applyFilters(): void {
    this.currentPage = 1;
    this.loadProducts();
  }

  resetFilters(): void {
    this.filterCategory = null;
    this.filterEstado = null;
    this.currentPage = 1;
    this.loadProducts();
  }

  onPageChange(page: number): void {
    this.currentPage = page;
    this.loadProducts();
  }

  getCategoryName(categoryId: number): string {
    const category = this.categories.find((c) => c.id === categoryId);
    return category ? category.nombre : 'Sin categoría';
  }
}
