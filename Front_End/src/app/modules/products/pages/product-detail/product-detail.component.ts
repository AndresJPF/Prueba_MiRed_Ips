import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Product } from '../../../../core/models/product.model';
import { Category } from '../../../../core/models/category.model';
import { ProductService } from '../../../../core/services/product.service';
import { CategoryService } from '../../../../core/services/category.service';

@Component({
  selector: 'app-product-detail',
  templateUrl: './product-detail.component.html',
  styleUrls: ['./product-detail.component.css']
})
export class ProductDetailComponent implements OnInit {
  product: Product | null = null;
  categories: Category[] = [];
  loading = false;
  error = '';

  constructor(
    private productService: ProductService,
    private categoryService: CategoryService,
    private route: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.loadCategories();
    this.route.params.subscribe(params => {
      if (params['id']) {
        this.loadProduct(params['id']);
      }
    });
  }

  loadCategories(): void {
    this.categoryService.getCategories().subscribe({
      next: (categories) => {
        this.categories = categories;
      },
      error: (err) => {
        console.error('Error al cargar categorías:', err);
      }
    });
  }

  loadProduct(id: number): void {
    this.loading = true;
    this.error = '';
    this.productService.getProduct(id).subscribe({
      next: (product) => {
        this.product = product;
        this.loading = false;
      },
      error: (err) => {
        this.error = 'Error al cargar el producto';
        this.loading = false;
        console.error(err);
      }
    });
  }

  getCategoryName(categoryId: number): string {
    const category = this.categories.find(c => c.id === categoryId);
    return category ? category.nombre : 'Sin categoría';
  }

  deleteProduct(): void {
    if (!this.product) return;
    if (!confirm('¿Estás seguro de eliminar este producto?')) return;

    this.productService.deleteProduct(this.product.id).subscribe({
      next: () => {
        this.router.navigate(['/products']);
      },
      error: (err) => {
        this.error = 'Error al eliminar el producto';
        console.error(err);
      }
    });
  }
}
