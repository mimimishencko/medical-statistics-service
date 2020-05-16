import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { InteractiveHelperComponent } from './interactive-helper.component';

describe('InteractiveHelperComponent', () => {
  let component: InteractiveHelperComponent;
  let fixture: ComponentFixture<InteractiveHelperComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ InteractiveHelperComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(InteractiveHelperComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
