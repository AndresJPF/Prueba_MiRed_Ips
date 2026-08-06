import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { ProductService } from '../../../../core/services/product.service';
import { CategoryService } from '../../../../core/services/category.service';
import { Category } from '../../../../core/models/category.model';

@Component({
  selector: 'app-product-form',
  templateUrl: './product-form.component.html',
  styleUrls: ['./product-form.component.css'],
})
export class ProductFormComponent implements OnInit {
  productForm: FormGroup;
  categories: Category[] = [];
  isEdit = false;
  productId = 0;
  loading = false;
  error = '';
  success = '';
  title = '';

  constructor(
    private fb: FormBuilder,
    private productService: ProductService,
    private categoryService: CategoryService,
    private route: ActivatedRoute,
    public router: Router,
  ) {
    this.productForm = this.fb.group({
      codigo: ['', [Validators.required]],
      nombre: ['', [Validators.required, Validators.minLength(3)]],
      categoria_id: ['', [Validators.required]],
      descripcion: [''],
      precio: ['', [Validators.required, Validators.min(0)]],
      stock: ['', [Validators.required, Validators.min(0)]],
      estado: ['activo', [Validators.required]],
    });
  }

  ngOnInit(): void {
    this.loadCategories();
    this.route.params.subscribe((params) => {
      if (params['id']) {
        this.isEdit = true;
        this.productId = params['id'];
        this.title = 'Editar Producto';
        this.loadProduct();
      } else {
        this.title = 'Nuevo Producto';
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
      },
    });
  }

  loadProduct(): void {
    this.loading = true;
    this.productService.getProduct(this.productId).subscribe({
      next: (product) => {
        this.productForm.patchValue({
          codigo: product.codigo,
          nombre: product.nombre,
          categoria_id: product.categoria_id,
          descripcion: product.descripcion,
          precio: product.precio,
          stock: product.stock,
          estado: product.estado,
        });
        this.loading = false;
      },
      error: (err) => {
        this.error = 'Error al cargar el producto';
        this.loading = false;
        console.error(err);
      },
    });
  }

  onSubmit(): void {
    if (this.productForm.invalid) return;

    this.loading = true;
    this.error = '';
    this.success = '';

    const formData = this.productForm.value;

    if (this.isEdit) {
      this.productService.updateProduct(this.productId, formData).subscribe({
        next: () => {
          this.loading = false;
          this.success = 'Producto actualizado exitosamente';
          setTimeout(() => this.router.navigate(['/products']), 2000);
        },
        error: (err) => {
          this.loading = false;
          this.error = err.error?.detail || 'Error al actualizar el producto';
        },
      });
    } else {
      this.productService.createProduct(formData).subscribe({
        next: () => {
          this.loading = false;
          this.success = 'Producto creado exitosamente';
          setTimeout(() => this.router.navigate(['/products']), 2000);
        },
        error: (err) => {
          this.loading = false;
          this.error = err.error?.detail || 'Error al crear el producto';
        },
      });
    }
  }
}
