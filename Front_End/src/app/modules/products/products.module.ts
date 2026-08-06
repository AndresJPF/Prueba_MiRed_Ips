import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ProductsRoutingModule } from './products-routing.module';
import { ProductListComponent } from './pages/product-list/product-list.component';
import { ProductFormComponent } from './pages/product-form/product-form.component';
import { ProductDetailComponent } from './pages/product-detail/product-detail.component';
import { SharedModule } from '../shared/shared.module';

@NgModule({
  declarations: [
    ProductListComponent,
    ProductFormComponent,
    ProductDetailComponent,
  ],
  imports: [
    CommonModule,
    ProductsRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    SharedModule,
  ],
})
export class ProductsModule {}
